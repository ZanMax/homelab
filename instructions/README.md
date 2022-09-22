# Instructions

#### Add new NVME drive

```bash
sudo lshw -C disk -short
```
##### Disk Partition From Command Line

```bash
sudo gdisk /dev/nvme0n1
```
Select **n** to add a new partition
Then just press ENTER
finally press **w** then **y** write table to disk and exit:

##### Format Disk ext4 from Command Line
```bash
sudo mkfs.ext4 /dev/nvme0n1
```
Check your drive
```bash
lsblk -f
```

##### Mount Drive
```bash
sudo blkid | grep nvme0n1
```
Copy UUID
```bash
sudo nano /etc/fstab
```
add string to the end of file:

```bash
UUID=c325f0bd-d9c7-4294-9eff-32cb77fed56a /mnt/data ext4 defaults 0 1
```

```bash
sudo mount -a
```

##### Setting the DNS Servers
```bash
sudo nano /etc/dhcpcd.conf
```

```bash
static domain_name_servers=8.8.4.4 8.8.8.8
```

```bash
sudo service dhcpcd restart
```


##### Sync Time
```bash
timedatectl status
```

```bash
timedatectl list-timezones | grep Canada
```

```bash
sudo timedatectl set-timezone Canada/Pacific
```

```bash
sudo apt install systemd-timesyncd
```

```bash
sudo timedatectl set-ntp true
```

Fix the delay now:

```bash
sudo service ntp stop
sudo ntpdate 0.us.pool.ntp.org
sudo service ntp start
```

##### Turn off LEDs

Blue LEDs
```bash
/sys/class/leds/user-led/brightness
```

Green LEDs
```bash
```