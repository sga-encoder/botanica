import psycopg2
import requests
from PIL import Image
import io
from transformers import CLIPProcessor, CLIPModel

print("-> Cargando modelo CLIP (esto puede tardar la primera vez)...")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# 1. CONEXIÓN A NEON
CONN_STR = "postgresql://neondb_owner:npg_EmcD06XptCSI@ep-misty-fire-aqij80ov-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

try:
    conn = psycopg2.connect(CONN_STR)
    cursor = conn.cursor()
    print("-> Conexión exitosa a Neon.")

    # 2. TRAER ENLACES (Cambiado a 'embedding' en singular según tu base de datos)
    cursor.execute("SELECT id_img, file_path FROM images WHERE embedding IS NULL;")
    filas = cursor.fetchall()
    print(f"-> Se encontraron {len(filas)} imágenes por procesar.")

    for id_img, file_path in filas:
        print(f"\nProcesando ID {id_img}...")
        url_directa = file_path

        # 3. DESCARGAR IMAGEN
        try:
            res = requests.get(url_directa, timeout=15)
            if res.status_code != 200:
                print(f"   [Error] Google Drive rechazó la descarga (Status: {res.status_code})")
                continue
            
            imagen = Image.open(io.BytesIO(res.content)).convert("RGB")
        except Exception as e:
            print(f"   [Error] Falló la descarga o lectura de la imagen: {e}")
            continue

        # 4. GENERAR EMBEDDING LOCAL (A prueba de balas y bucles)
        inputs = processor(images=imagen, return_tensors="pt")
        
        # Usamos el método nativo de visión
        outputs = model.get_image_features(**inputs)
        
        # Interrogamos al objeto: Si es el contenedor molesto, le sacamos el tensor real
        if hasattr(outputs, 'image_embeds'):
            tensor_puro = outputs.image_embeds
        elif hasattr(outputs, 'pooler_output'):
            tensor_puro = outputs.pooler_output
        elif isinstance(outputs, dict) and 'image_embeds' in outputs:
            tensor_puro = outputs['image_embeds']
        else:
            # Si ya es un tensor plano por defecto
            tensor_puro = outputs

        # Ahora sí, a este tensor limpio le aplicamos el detach sin riesgo de error
        embedding_vector = tensor_puro.detach().cpu().numpy()[0].tolist()

        # 5. GUARDAR EN NEON
        cursor.execute(
            "UPDATE images SET embedding = %s WHERE id_img = %s;",
            (embedding_vector, id_img)
        )
        conn.commit()
        print(f"   [Éxito] Embedding guardado para ID {id_img}.")

except Exception as error:
    print(f"Error general en la ejecución: {error}")
finally:
    if 'conn' in locals() and conn:
        cursor.close()
        conn.close()
        print("\n-> Conexión cerrada.")