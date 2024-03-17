from django.db import models


class CoinFlip(models.Model):
    # side_choices = f"h":{heds}, "s":{}
    side = models.CharField(max_length=5)
    time_temp = models.DateTimeField(auto_now=True)


@staticmethod
def get_last_n_flips(n):
    last_n_flips = CoinFlip.objects.order_by('-time_stemp')[:n]
    count_heads = count_tails = 0
    for flip in last_n_flips:
        if flip.side == 'tails':
            count_tails += 1
        else:
            count_heads += 1
    return {'count_heads': count_heads, 'count_tails': count_tails}
