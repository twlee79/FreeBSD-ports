# Created by: lbartoletti <lbartoletti@tuxfamily.org>
# $FreeBSD$

PORTNAME=	libght
PORTVERSION=	0.1.0
PORTREVISION=	1
DISTVERSIONPREFIX=	v
CATEGORIES=	devel geography

MAINTAINER=	lbartoletti@tuxfamily.org
COMMENT=	GeoHashTree library for storing and accessing multi-dimensional point clouds

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/COPYRIGHT

LIB_DEPENDS=	libproj.so:graphics/proj \
		liblas.so:devel/liblas \
		libcunit.so:devel/cunit

USES=		cmake
USE_GNOME=	libxml2
USE_LDCONFIG=	yes
CFLAGS+=	"-DACCEPT_USE_OF_DEPRECATED_PROJ_API_H=1"

USE_GITHUB=	yes
GH_ACCOUNT=	pramsey

.include <bsd.port.mk>
