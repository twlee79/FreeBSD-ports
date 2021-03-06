# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD$

PORTNAME=	openstacksdk
PORTVERSION=	0.17.0
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	alexander.nusov@nfvexpress.com
COMMENT=	Unified SDK for OpenStack

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr@${PY_FLAVOR}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}yaml>=3.10:devel/py-yaml@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}appdirs>=1.3.0:devel/py-appdirs@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requestsexceptions>=1.2.0:devel/py-requestsexceptions@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}jsonpatch>=1.16:devel/py-jsonpatch@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}six>=1.10.0:devel/py-six@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}os-service-types>=1.1.0:devel/py-os-service-types@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}keystoneauth1>=3.3.0:devel/py-keystoneauth1@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}deprecation>=1.0:devel/py-deprecation@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}munch>=2.1.0:devel/py-munch@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}decorator>=3.4.0:devel/py-decorator@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}jmespath>=0.9.0:devel/py-jmespath@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}iso8601>=0.1.11:devel/py-iso8601@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}netifaces>=0.10.4:net/py-netifaces@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}dogpile.cache>=0.6.2:devel/py-dogpile.cache@${PY_FLAVOR} \
		${PY_FUTURES} \
		${PY_IPADDRESS}

USES=		python shebangfix
USE_PYTHON=	distutils autoplist
SHEBANG_FILES=	openstack/tests/functional/cloud/hooks/post_test_hook.sh

NO_ARCH=	yes

.include <bsd.port.mk>
