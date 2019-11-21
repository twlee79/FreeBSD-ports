# pfSense port created by: Tet Woo Lee <developer@twlee.nz>
# FreeBSD port created by: Sean Greven <sean.greven@gmail.com>
# $FreeBSD$

PORTNAME=		fwknop
PORTVERSION=	2.6.10
PORTREVISION=	1
CATEGORIES=		security
MASTER_SITES=	http://www.cipherdyne.org/fwknop/download/

MAINTAINER=		developer@twlee.nz
COMMENT=		SPA implementation for pfSense

LICENSE=		GPLv2

USES=			cpe libtool
USE_LDCONFIG=	yes
USE_RC_SUBR=	fwknopd

CPE_VENDOR=		cipherdyne
CONFLICTS_BUILD=fwknop-2.6.8_*

GNU_CONFIGURE=	yes

INSTALL_TARGET=	install-strip
INFO=			libfko

CONFIGURE_ARGS= --with-gpgme=no --with-pf=/sbin/pfctl --disable-client 

post-install:
	(cd ${STAGEDIR}${PREFIX}/etc/fwknop && ${MV} access.conf access.conf.sample)
	(cd ${STAGEDIR}${PREFIX}/etc/fwknop && ${MV} fwknopd.conf fwknopd.conf.sample)

.include <bsd.port.mk>
