class Dechargestore():
    decharges = []
    last_num = 1

    def get_all(self):
        return Dechargestore.decharges

    def add(self, decharge):
        decharge.num = Dechargestore.last_num
        Dechargestore.decharges.append(decharge)

    def get_by_num(self, num):
        result = None
        for decharge in Dechargestore.decharges:
            if num == decharge.num:
                result =  decharge
                break
        return result

    def update(self, decharge):
        for index, decharge_to_update in enumerate(Dechargestore.decharges):
            if decharge.id == decharge_to_update.id:
                Dechargestore.decharges[index] = decharge
                break

    def delete(self, id):
        Dechargestore.decharges.remove(self.get_by_id(id))

    def entity_exists(self, decharge):
        result = True
        if self.get_by_id(decharge.id) is None:
            result = False
        return result



