# Created by: Johannes Meixner <johannes@perceivon.net>
# $FreeBSD$

PORTNAME=	libgcrypt
PORTVERSION=	1.4.5
DISTVERSIONSUFFIX=	-12.el6_8
PORTREVISION=	7
CATEGORIES=	security linux

MAINTAINER=	emulation@FreeBSD.org
COMMENT=	General purpose crypto library based on code used in GnuPG (Linux CentOS ${LINUX_DIST_VER})

USES=		linux:c6
USE_LDCONFIG=	yes
USE_LINUX=	libgpg-error
USE_LINUX_RPM=	yes

DESCR=		${.CURDIR}/../${PORTNAME}/pkg-descr

OPTIONS_DEFINE=	DOCS

.include <bsd.port.mk>
