# $FreeBSD$

PORTNAME=	lumina-photo
DISTVERSIONPREFIX=	v
DISTVERSION=	1.5.0
CATEGORIES=	deskutils

MAINTAINER=	jt@ixsystems.com
COMMENT=	Image viewer utility from the Lumina Desktop

LICENSE=	BSD3CLAUSE

USES=		qmake qt:5
USE_QT=		buildtools_build concurrent core gui multimedia \
		network svg widgets x11extras
USE_GITHUB=	yes
GH_ACCOUNT=	lumina-desktop
GH_PROJECT=	lumina

OPTIONS_DEFINE=		NLS
OPTIONS_SUB=		yes

WRKSRC_SUBDIR=	src-qt5/desktop-utils/${PORTNAME}

NLS_USE=	QT=linguist_build
NLS_QMAKE_ON=	CONFIG+=WITH_I18N

.include <bsd.port.mk>
