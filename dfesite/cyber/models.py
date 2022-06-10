from django.db import models

# Create your models here.
class Comp_Name(models.Model):
    comp_name = models.CharField(max_length=256)

    def __str__(self):
        return self.comp_name

class ServerName(models.Model):
    server_name = models.CharField(max_length=256)

    def __str__(self):
        return self.server_name


class CPU(models.Model):
    cpu = models.CharField(max_length=256)

    def __str__(self):
        return self.cpu


class Mainboard(models.Model):
    mb_model = models.CharField(max_length=256)

    def __str__(self):
        return self.mb_model


class RAM(models.Model):
    ram_model = models.CharField(max_length=256)
    ram_type = models.CharField(max_length=20, help_text="DDR3-2400, DDR4-3200 или др.")
    ram_formfactor = models.CharField(max_length=10, help_text="DIMM, SO-DIMM или др.")
    ram_capacity = models.IntegerField(help_text="Размер диска в Гб")

    def __str__(self):
        return f"{self.ram_model} {self.ram_capacity}Гб"


class SSD(models.Model):
    ssd_model = models.CharField(max_length=256)
    ssd_formfactor = models.CharField(max_length=20, help_text='2.5", NVMe M.2 или др.')
    ssd_capacity = models.IntegerField(help_text="Размер диска в Гб")

    def __str__(self):
        return f"{self.ssd_model} {self.ssd_capacity}Гб"


class HDD(models.Model):
    hdd_model = models.CharField(max_length=256)
    hdd_formfactor = models.CharField(max_length=20, help_text='2.5", 3.5"')
    hdd_capacity = models.IntegerField(help_text="Размер диска в Гб")

    def __str__(self):
        return f"{self.hdd_model} {self.hdd_capacity}Гб"


class PowerUnit(models.Model):
    pu_model = models.CharField(max_length=256)
    pu_watt = models.IntegerField(help_text='Мощность (номинал)')

    def __str__(self):
        return f"{self.pu_model} {self.pu_watt}Вт"


class Monitor(models.Model):
    monitor_model = models.CharField(max_length=256)
    monitor_size = models.FloatField(help_text='24" (диагональ в дюймах)')
    monitor_resolution = models.CharField(max_length=10, help_text='1920x1080 (разрешение)')

    def __str__(self):
        return f'{self.monitor_model} {self.monitor_size}" {self.monitor_resolution}'


class NetAdapter(models.Model):
    adapter_model = models.CharField(max_length=256)
    adapter_speed = models.IntegerField(help_text='Скорость в Мбит/сек')

    def __str__(self):
        return f"{self.adapter_model} {self.adapter_speed} Мбит/сек"


class PC(models.Model):
    pc_name = models.ForeignKey(Comp_Name, on_delete=models.CASCADE, verbose_name="Имя ПК")
    pc_cpu = models.ForeignKey(CPU, on_delete=models.CASCADE, verbose_name="Процессор")
    pc_mainboard = models.ForeignKey(Mainboard, on_delete=models.CASCADE, verbose_name="Материнская плата")
    pc_ram = models.ForeignKey(RAM, on_delete=models.CASCADE, verbose_name="Оперативная память")
    pc_ssd = models.ForeignKey(SSD, on_delete=models.CASCADE, verbose_name="SSD")
    pc_hdd = models.ForeignKey(HDD, on_delete=models.CASCADE, verbose_name="HDD")
    pc_powerunit = models.ForeignKey(PowerUnit, on_delete=models.CASCADE, verbose_name="Блок питания")
    pc_monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE, verbose_name="Монитор")

    pc_location = models.CharField(max_length=256, help_text='Местонахождение', verbose_name="Местонахождение")
    pc_os = models.CharField(max_length=256, help_text='Операционная система', verbose_name="Операционная система")
    pc_netnum = models.IntegerField(default=1, help_text='Количество сетевых адаптеров', verbose_name="Количество сетевых адаптеров")
    pc_netnum.value_from_object()
    pc_net = list()
    for num in pc_netnum:
        pc_net[num] = models.ForeignKey(NetAdapter, on_delete=models.CASCADE, verbose_name=f"Сетевой адаптер {num+1}")
    pc_inventory = models.CharField(max_length=50, help_text='Инвентарный номер', verbose_name="Инвентарный номер")
