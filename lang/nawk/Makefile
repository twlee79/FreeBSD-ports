# Created by: Josh Gilliam <josh@quick.net>
# $FreeBSD$

PORTNAME=	nawk
PORTVERSION=	20121220
CATEGORIES=	lang
MASTER_SITES=	http://www.cs.princeton.edu/~bwk/btl.mirror/
DISTNAME=	awk
DIST_SUBDIR=	nawk-${PORTVERSION}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Brian Kernighan's pattern scanning and processing language

BROKEN=		unfetchable
DEPRECATED=	Unfetchable, unmaintained
EXPIRATION_DATE=	2019-10-16

NO_WRKSUBDIR=	yes
MAKEFILE=	makefile
ALL_TARGET=	a.out
CFLAGS+=	-DHAS_ISBLANK
PLIST_FILES=	bin/nawk man/man1/nawk.1.gz

post-patch:
	@${REINPLACE_CMD} -e 's|awk|nawk|g' ${WRKSRC}/awk.1

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/a.out ${STAGEDIR}${PREFIX}/bin/nawk
	${INSTALL_MAN} ${WRKSRC}/awk.1 \
		${STAGEDIR}${MANPREFIX}/man/man1/nawk.1.gz

.include <bsd.port.mk>
