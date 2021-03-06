# $FreeBSD$

PORTNAME=	k40-whisperer
DISTVERSION=	0.37
CATEGORIES=	cad python
MASTER_SITES=	http://www.scorchworks.com/K40whisperer/
DISTNAME=	K40_Whisperer-${DISTVERSION}_src

MAINTAINER=	0mp@FreeBSD.org
COMMENT=	GUI control software for the stock K40 laser cutter controller

LICENSE=	GPLv3+
LICENSE_FILE=	${WRKSRC}/gpl-3.0.txt

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}lxml>0:devel/py-lxml@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pillow>0:graphics/py-pillow@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}usb>0:devel/py-usb@${PY_FLAVOR}

USES=		python:run,-3.7 shebangfix zip
SHEBANG_FILES=	*.py

NO_ARCH=	yes
NO_BUILD=	yes

DESKTOP_ENTRIES=	"K40 Whisperer" "${COMMENT}" \
			"${DATADIR}/scorchworks.ico" "${WHISPERER_COMMAND}" \
			"Development;Art;Engineering;VectorGraphics;" false

PLIST_SUB=	WHISPERER_COMMAND=${WHISPERER_COMMAND}
SUB_FILES=	pkg-message ${WHISPERER_COMMAND}
SUB_LIST=	PYTHON_CMD=${PYTHON_CMD} WHISPERER_COMMAND=${WHISPERER_COMMAND}

OPTIONS_DEFINE=	DOCS

DOCS=		Change_Log.txt \
		README_Linux.txt \
		README_MacOS.md
NON_DATA_FILES=	${DOCS} \
		${LICENSE_FILE:S,${WRKSRC}/,,} \
		build_exe.bat \
		py2exe_setup.py \
		requirements.txt
WHISPERER_COMMAND=	${PORTNAME}

do-install:
	${INSTALL_SCRIPT} ${WRKDIR}/${WHISPERER_COMMAND} ${STAGEDIR}${PREFIX}/bin
	@${MKDIR} ${STAGEDIR}${DATADIR}
	(cd ${WRKSRC} && ${COPYTREE_SHARE} . \
		${STAGEDIR}${DATADIR} "${NON_DATA_FILES:S,^,! -name &,}")
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${DOCS:S,^,${WRKSRC}/,} ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
