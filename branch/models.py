from django.db import models
import uuid


class BranchModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.TextField(null=False)
    url = models.TextField(default=None, null=False)
    explanation = models.TextField(null=True)
    metric = models.ManyToManyField('BranchMetric', blank=True)

    def get_metrics(self):
        return self.metric.all().order_by("calculation_time")

    def get_last_metric(self):
        return self.get_metrics().first()


class BranchMetric(models.Model):
    sincere_count = models.IntegerField(default=0)
    reputable_count = models.IntegerField(default=0)
    powerful_count = models.IntegerField(default=0)
    competence_count = models.IntegerField(default=0)
    excitement_count = models.IntegerField(default=0)
    negative_count = models.IntegerField(default=0)

    repetitive_words = models.JSONField(blank=True, null=True)
    calculation_time = models.DateField(auto_now=True)

    def get_counts_with_name(self):
        return {
            'sincere_count': self.sincere_count,
            'reputable_count': self.reputable_count,
            'powerful_count': self.powerful_count,
            'competence_count': self.competence_count,
            'excitement_count': self.excitement_count,
        }

    def get_total_metric(self):
        return sum(self.get_counter_counts().values())

    def get_metric_as_percentile_ord_isgyh(self):
        total = self.get_total_metric()
        result: list = []
        for count in self.get_counter_counts():
            count: dict = count
            k, v = count.items()
            result.append(
                int(round((v / total) * 100, 2)),
            )
        return result

    def get_metric(self):
        total = self.get_total_metric()
        return [
            {"name": "sincere", "result": round((self.sincere_count / total) * 100, 2)},  # içten
            {"name": "reputable", "result": round((self.reputable_count / total) * 100, 2)},  # saygınlık
            {"name": "powerful", "result": round((self.powerful_count / total) * 100, 2)},  # güç
            {"name": "competence", "result": round((self.competence_count / total) * 100, 2)},  # yetkinlik
            {"name": "excitement", "result": round((self.excitement_count / total) * 100, 2)},  # heyecan
            {"name": "negative", "result": round((self.negative_count / total) * 100, 2)},  # olumsuz
        ]

    def get_counter_counts(self):
        counter_counts: dict = {}
        for k, v in self.__dict__.items():
            if k.endswith("count"):
                counter_counts[k] = v
        return counter_counts


