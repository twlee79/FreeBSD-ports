--- deps/openssl/config/archs/linux-elf/asm/openssl-cl.gypi.orig	2019-07-31 17:44:59 UTC
+++ deps/openssl/config/archs/linux-elf/asm/openssl-cl.gypi
@@ -25,12 +25,11 @@
     ],
     'openssl_cflags_linux-elf': [
       '-Wa,--noexecstack',
-      '-Wall -O3 -fomit-frame-pointer',
+      '-Wall -O3',
       '-pthread',
-      '-Wall -O3 -fomit-frame-pointer',
     ],
     'openssl_ex_libs_linux-elf': [
-      '-ldl -pthread',
+      '',
     ],
     'openssl_cli_srcs_linux-elf': [
       'openssl/apps/asn1pars.c',
