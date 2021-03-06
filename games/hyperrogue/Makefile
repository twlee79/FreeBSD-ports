# Created by: Dmitry Marakasov <amdmi3@FreeBSD.org>
# $FreeBSD$

PORTNAME=	hyperrogue
PORTVERSION=	10.5e
PORTREVISION=	1
DISTVERSIONPREFIX=	v
CATEGORIES=	games

MAINTAINER=	amdmi3@FreeBSD.org
COMMENT=	Roguelike in a non-euclidean world

LICENSE=	GPLv2+
LICENSE_FILE=	${WRKSRC}/COPYING

LIB_DEPENDS=	libpng.so:graphics/png

USE_GITHUB=	yes
GH_ACCOUNT=	zenorogue

USES=		autoreconf compiler:c++11-lang gl localbase sdl
GNU_CONFIGURE=	yes
USE_SDL=	sdl mixer gfx ttf
USE_GL=		gl glew

# remove -O2, otherwise clang takes gigabytes of memory
CFLAGS:=	${CFLAGS:C/-O[0-9]//} -DFHS
CXXFLAGS:=	${CXXFLAGS:C/-O[0-9]//} -DFHS

PORTDOCS=	README.md

DESKTOP_ENTRIES="HyperRogue" \
		"" \
		"${PREFIX}/share/pixmaps/${PORTNAME}.ico" \
		"${PORTNAME}" \
		"Game;RolePlaying;" \
		""

OPTIONS_DEFINE=	DOCS

post-patch:
	@${REINPLACE_CMD} -e 's|isnumber|is_number|' ${WRKSRC}/archimedean.cpp

post-install:
	${INSTALL_DATA} ${WRKSRC}/hr-icon.ico ${STAGEDIR}${PREFIX}/share/pixmaps/${PORTNAME}.ico

post-install-DOCS-on:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/README.md ${STAGEDIR}${DOCSDIR}/

.include <bsd.port.mk>
