# Created by: David Naylor <dbn@FreeBSD.org>
# $FreeBSD$

PORTNAME=	libunwind
PORTVERSION=	1.1
DISTVERSIONSUFFIX=	-3.el6
CATEGORIES=	devel linux
MASTER_SITES=	EPEL/l

MAINTAINER=	emulation@FreeBSD.org
COMMENT=	Generic stack unwinding library (Linux CentOS ${LINUX_DIST_VER})

USES=		linux:c6
USE_LDCONFIG=	yes
USE_LINUX_RPM=	yes

DESCR=		${.CURDIR}/../${PORTNAME}/pkg-descr

OPTIONS_DEFINE=	DOCS

.include <bsd.port.mk>
