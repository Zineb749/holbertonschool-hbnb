from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}
        self.data = {}
        
    def add(self, obj):
        print(f"🛠 DEBUG : Ajout de l'objet {obj.id} -> {obj}")
        self.data[obj.id] = obj  # ✅ Maintenant, on stocke dans `data`
        print(f"📌 DEBUG : Contenu de data après ajout -> {self.data.keys()}")
    def get(self, obj_id):
        print(f"🔍 DEBUG : Recherche de {obj_id} dans data : {self.data.keys()}")
        return self.data.get(str(obj_id))  # ✅ Recherche dans `data`

    def get_all(self):
        print(f"📌 DEBUG : Récupération de toutes les entrées depuis data : {self.data.keys()}")
        return list(self.data.values())  # ✅ Retourne toutes les valeurs de `data`


    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            if not isinstance(data, dict):
                data = data.__dict__
            
            for key, value in data.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            
            self.data[obj_id] = obj  # ✅ Met à jour l'objet dans `data`
            print(f"📌 DEBUG : Objet {obj_id} mis à jour dans data.")
        return obj


    def delete(self, obj_id):
        if obj_id in self.data:
            del self.data[obj_id]  # ✅ Supprime l'objet de `data`
            print(f"🗑 DEBUG : Objet {obj_id} supprimé de data.")

    def get_by_attribute(self, attr_name, attr_value):
        return next((obj for obj in self.data.values() if getattr(obj, attr_name) == attr_value), None)

        
    def save(self, obj):
        print(f"💾 DEBUG : Sauvegarde de l'objet {obj.id} dans data.")
        self.data[obj.id] = obj  # ✅ Stocker dans `data` au lieu de `_storage`
        print(f"📌 DEBUG : Contenu de data après sauvegarde -> {self.data.keys()}")


    def get_by_place_id(self, place_id):
        """Récupère un propriétaire via l'ID du lieu"""
        for owner in self.data.values():
            if owner.get("place_id") == place_id:
                return owner
        return None  
    
    def get_reviews_by_place_id(self, place_id):
        return [review for review in self.data.values() if str(review.place_id) == str(place_id)]

