"""
Botanica Domain Module

Exporta todos los servicios y repositorios del sistema para acceso centralizado.
"""

# Services
from .services import (
    BaseRepositoryService,
    UserService,
    RoleService,
    SessionService,
    FamilyService,
    GenusService,
    SpeciesService,
    DocumentService,
    ChunkService,
    AltitudinalRangeService,
    SpeciesUsagesService,
    UsagesService,
    EmbeddingImageService,
    ImageService,
    EmbeddingTextService,
    QueryService,
    EvaluationService
)

# Repositories
from .repositories import (
    UserRepository,
    RoleRepository,
    SessionRepository,
    FamilyRepository,
    GenusRepository,
    SpeciesRepository,
    DocumentRepository,
    ChunkRepository,
    AltitudinalRangeRepository,
    SpeciesUsagesRepository,
    UsagesRepository,
    EmbeddingImageRepository,
    ImageRepository,
    EmbeddingTextRepository,
    QueryRepository,
    EvaluationRepository,
    BaseRepository
)

__all__ = [
    # Services
    "BaseRepositoryService",
    "UserService",
    "RoleService",
    "SessionService",
    "FamilyService",
    "GenusService",
    "SpeciesService",
    "DocumentService",
    "ChunkService",
    "AltitudinalRangeService",
    "SpeciesUsagesService",
    "UsagesService",
    "EmbeddingImageService",
    "ImageService",
    "EmbeddingTextService",
    "QueryService",
    "EvaluationService",
    # Repositories
    "UserRepository",
    "RoleRepository",
    "SessionRepository",
    "FamilyRepository",
    "GenusRepository",
    "SpeciesRepository",
    "DocumentRepository",
    "ChunkRepository",
    "AltitudinalRangeRepository",
    "SpeciesUsagesRepository",
    "UsagesRepository",
    "EmbeddingImageRepository",
    "ImageRepository",
    "EmbeddingTextRepository",
    "QueryRepository",
    "EvaluationRepository",
    "BaseRepository"
]
