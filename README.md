#### PyCPU - Central Processing Unit Information Gathering Tool

With this tool you can access detailed information of your processor information. You can also check the security vulnerability based on the current processor information of the processor you have used.

#### Programming Languages :

* Python

#### System :

* Linux

#### What is CPU ( Central Processing Unit ) ?

A central processing unit (CPU) is the electronic circuitry within a computer that carries out the instructions of a computer program by performing the basic arithmetic, logic, controlling and input/output (I/O) operations specified by the instructions.

#### RUN

```
root@ismailtasdelen:~# git clone https://github.com/ismailtasdelen/PyCPU.git
root@ismailtasdelen:~# cd PyCPU
root@ismailtasdelen:~/PyCPU# python PyCPU.py
```

#### What's on the tool menu ?

```
[1] CPU All Information Gathering
[2] Default Information Gathering
[3] CPU Vulnerability Check
[4] Exit
```

all_cpu() --> call the function. actually this function is`cat /proc/cpuinfo` running the code in the system. we can access all information.

```
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 69
model name	: Intel(R) Core(TM) i5-4210U CPU @ 1.70GHz
stepping	: 1
microcode	: 0x1c
cpu MHz		: 1700.062
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm epb tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt dtherm ida arat pln pts
bugs		:
bogomips	: 4788.92
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:
......
```

The cpu_info() function shows some simple cpu information.

```
vendor_id	: GenuineIntel
model name	: Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz
microcode	: 0x24
cpu MHz		: 2446.218
cpu MHz		: 2574.107
cpu MHz		: 2294.998
cpu MHz		: 2295.091
cache size	: 3072 KB
```

The cpu_vulncheck() function performs the vulnerability check on the computer you are running.

```
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf
```

#### Cloning an Existing Repository ( Clone with HTTPS )

```
root@ismailtasdelen:~# git clone https://github.com/ismailtasdelen/PyCPU.git
```

#### Cloning an Existing Repository ( Clone with SSH )

```
root@ismailtasdelen:~# git clone https://github.com/ismailtasdelen/PyCPU.git
```

#### Contact :

```
Mail : ismailtasdelen@protonmail.com
Linkedin : https://www.linkedin.com/in/ismailtasdelen
GitHub : https://github.com/ismailtasdelen
Telegram : https://t.me/ismailtasdelen
```
