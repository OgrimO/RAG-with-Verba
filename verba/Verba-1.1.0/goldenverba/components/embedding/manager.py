from wasabi import msg
from weaviate import WeaviateClient

from goldenverba.components.embedding.ADAEmbedder import ADAEmbedder
from goldenverba.components.embedding.CohereEmbedder import CohereEmbedder
from goldenverba.components.embedding.interface import Embedder
from goldenverba.components.embedding.MiniLMEmbedder import MiniLMEmbedder
from goldenverba.components.reader.document import Document


class EmbeddingManager:
    def __init__(self):
        self.embedders: dict[str, Embedder] = {
            "MiniLMEmbedder": MiniLMEmbedder(),
            "ADAEmbedder": ADAEmbedder(),
            "CohereEmbedder": CohereEmbedder(),
        }
        self.selected_embedder: Embedder = self.embedders["ADAEmbedder"]

    def embed(
        self, documents: list[Document], client: WeaviateClient, batch_size: int = 100
    ) -> bool:
        """Embed verba documents and its chunks to Weaviate
        @parameter: documents : list[Document] - List of Verba documents
        @parameter: client : Client - Weaviate Client
        @parameter: batch_size : int - Batch Size of Input
        @returns bool - Bool whether the embedding what successful.
        """
        return self.selected_embedder.embed(documents, client)

    def set_embedder(self, embedder: str) -> bool:
        if embedder in self.embedders:
            self.selected_embedder = self.embedders[embedder]
            return True
        else:
            msg.warn(f"Embedder {embedder} not found")
            return False

    def get_embedders(self) -> dict[str, Embedder]:
        return self.embedders
