import json
import os

class PopulationSearcher:

    def __init__(self):
        self.subjects = None

    def _load_subjects(self):
        filepath = os.path.dirname(os.path.abspath(__file__)) + '/russian-cities.json'
        with open(filepath) as json_file:
            raw_cities = json.load(json_file)
            subjects = {}

            for city in raw_cities:
                city_name = self._process_city(city['name'])
                subject_name = self._process_subject(city['subject'])

                if subject_name not in subjects:
                    subjects[subject_name] = {}

                if city_name not in subjects[subject_name]:
                    subjects[subject_name][city_name] = city['population']
                else:
                    raise Exception('City ' + city_name + ' already exists')

            return subjects

    def search(self, subject, city):
        if self.subjects is None:
            self.subjects = self._load_subjects()

        processed_city = self._process_city(city)
        processed_subject = self._process_subject(subject)
        if (processed_subject in self.subjects) and (processed_city in self.subjects[processed_subject]):
            return self.subjects[processed_subject ][processed_city]

        return None

    def _common_process(self, name):
        processed = name.lower()
        bad_chars = '?!-,./()'
        processed = ''.join(c for c in processed if c not in bad_chars)
        processed = ' '.join(processed.split())

        processed = processed.replace('ё', 'е')

        return processed

    def _process_subject(self, subject):
        processed = self._common_process(subject)

        for_skipping = ['республика', 'область', 'край']
        processed = ' '.join([word for word in processed.split() if word not in for_skipping])

        processed = processed.replace('автономный округ', 'ао')
        processed = processed.replace('московская', 'москва')
        processed = processed.replace('сочи', 'краснодарский')
        processed = processed.replace('ленинградская', 'санктпетербург')
        processed = processed.replace('саха якутия', 'якутия')

        return processed

    def _process_city(self, city):
        processed = self._common_process(city)
        for_skipping = ['город', 'г', 'край']
        processed = ' '.join([word for word in processed.split() if word not in for_skipping])

        return processed