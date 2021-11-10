from pynamodb.attributes import ListAttribute, MapAttribute, NumberAttribute


class ModelIterator:
    def __iter__(self):
        for name, attr in self.get_attributes().items():
            if isinstance(attr, MapAttribute):
                yield name, getattr(self, name).as_dict()
            if isinstance(attr, ListAttribute):
                results = []
                for el in getattr(self, name):
                    if isinstance(el, MapAttribute):
                        results.append((el.as_dict()))
                    else:
                        results.append(el)
                yield name, results
            elif isinstance(attr, NumberAttribute):
                yield name, getattr(self, name)
            else:
                yield name, attr.serialize(getattr(self, name))
