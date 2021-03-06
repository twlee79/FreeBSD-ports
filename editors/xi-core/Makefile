# $FreeBSD$

PORTNAME=	xi-core
DISTVERSION=	g20190420
PORTREVISION=	5
CATEGORIES=	editors

MAINTAINER=	ed.arrakis@gmail.com
COMMENT=	Modern editor backend written in Rust

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/../LICENSE

USES=		cargo
USE_GITHUB=	yes
GH_ACCOUNT=	xi-editor
GH_PROJECT=	xi-editor
GH_TAGNAME=	c16973f
GH_TUPLE=	trishume:syntect:24887e407957438282e4183e3dfe80a086e01530:syntect

CARGO_CRATES=	adler32-1.0.3 \
		aho-corasick-0.7.3 \
		argon2rs-0.2.5 \
		arrayref-0.3.5 \
		arrayvec-0.4.10 \
		ascii-0.9.1 \
		autocfg-0.1.2 \
		backtrace-0.3.15 \
		backtrace-sys-0.1.28 \
		base64-0.10.1 \
		bincode-1.1.3 \
		bitflags-0.7.0 \
		bitflags-1.0.4 \
		blake2-rfc-0.2.18 \
		block-buffer-0.3.3 \
		build_const-0.2.1 \
		byte-tools-0.2.0 \
		bytecount-0.5.1 \
		byteorder-1.3.1 \
		cc-1.0.35 \
		cfg-if-0.1.7 \
		chrono-0.4.6 \
		cloudabi-0.0.3 \
		combine-3.8.1 \
		constant_time_eq-0.1.3 \
		crc-1.8.1 \
		crc32fast-1.2.0 \
		crossbeam-0.7.1 \
		crossbeam-channel-0.3.8 \
		crossbeam-deque-0.7.1 \
		crossbeam-epoch-0.7.1 \
		crossbeam-queue-0.1.2 \
		crossbeam-utils-0.6.5 \
		digest-0.7.6 \
		dirs-1.0.5 \
		either-1.5.2 \
		failure-0.1.5 \
		failure_derive-0.1.5 \
		fake-simd-0.1.2 \
		fern-0.5.8 \
		filetime-0.2.4 \
		flate2-1.0.7 \
		fnv-1.0.6 \
		fsevent-0.2.17 \
		fsevent-sys-0.1.6 \
		fuchsia-cprng-0.1.1 \
		fuchsia-zircon-0.3.3 \
		fuchsia-zircon-sys-0.3.3 \
		generic-array-0.9.0 \
		humantime-1.2.0 \
		idna-0.1.5 \
		inotify-0.6.1 \
		inotify-sys-0.1.3 \
		iovec-0.1.2 \
		itoa-0.4.3 \
		jsonrpc-lite-0.5.0 \
		kernel32-sys-0.2.2 \
		languageserver-types-0.54.0 \
		lazy_static-1.3.0 \
		lazycell-1.2.1 \
		libc-0.2.51 \
		line-wrap-0.1.1 \
		linked-hash-map-0.5.2 \
		log-0.4.6 \
		matches-0.1.8 \
		memchr-2.2.0 \
		memoffset-0.2.1 \
		miniz-sys-0.1.11 \
		miniz_oxide-0.2.1 \
		miniz_oxide_c_api-0.2.1 \
		mio-0.6.16 \
		mio-extras-2.0.5 \
		miow-0.2.1 \
		net2-0.2.33 \
		nodrop-0.1.13 \
		nom-4.2.3 \
		notify-4.0.10 \
		num-derive-0.2.4 \
		num-integer-0.1.39 \
		num-traits-0.2.6 \
		onig-4.3.2 \
		onig_sys-69.1.0 \
		percent-encoding-1.0.1 \
		pkg-config-0.3.14 \
		plist-0.4.1 \
		pom-3.0.2 \
		proc-macro2-0.4.27 \
		quick-error-1.2.2 \
		quote-0.6.12 \
		rand-0.4.6 \
		rand-0.6.5 \
		rand_chacha-0.1.1 \
		rand_core-0.3.1 \
		rand_core-0.4.0 \
		rand_hc-0.1.0 \
		rand_isaac-0.1.1 \
		rand_jitter-0.1.3 \
		rand_os-0.1.3 \
		rand_pcg-0.1.2 \
		rand_xorshift-0.1.1 \
		rdrand-0.4.0 \
		redox_syscall-0.1.54 \
		redox_users-0.3.0 \
		regex-1.1.5 \
		regex-syntax-0.6.6 \
		remove_dir_all-0.5.1 \
		rustc-demangle-0.1.14 \
		ryu-0.2.7 \
		safemem-0.3.0 \
		same-file-1.0.4 \
		scoped_threadpool-0.1.9 \
		scopeguard-0.3.3 \
		serde-1.0.90 \
		serde_derive-1.0.90 \
		serde_json-1.0.39 \
		serde_test-1.0.90 \
		sha2-0.7.1 \
		slab-0.4.2 \
		smallvec-0.6.9 \
		syn-0.15.30 \
		synstructure-0.10.1 \
		syntect-3.2.0 \
		tempdir-0.3.7 \
		thread_local-0.3.6 \
		time-0.1.42 \
		toml-0.5.0 \
		typenum-1.10.0 \
		ucd-util-0.1.3 \
		unicode-bidi-0.3.4 \
		unicode-normalization-0.1.8 \
		unicode-segmentation-1.2.1 \
		unicode-xid-0.1.0 \
		unreachable-1.0.0 \
		url-1.7.2 \
		url_serde-0.2.0 \
		utf8-ranges-1.0.2 \
		version_check-0.1.5 \
		void-1.0.2 \
		walkdir-2.2.7 \
		winapi-0.2.8 \
		winapi-0.3.7 \
		winapi-build-0.1.1 \
		winapi-i686-pc-windows-gnu-0.4.0 \
		winapi-util-0.1.2 \
		winapi-x86_64-pc-windows-gnu-0.4.0 \
		ws2_32-sys-0.2.1 \
		xml-rs-0.8.0 \
		yaml-rust-0.4.3

CARGO_USE_GITHUB=	yes

WRKSRC_SUBDIR=	rust

PLIST_FILES=	bin/xi-core
PORTDOCS=	README.md

OPTIONS_DEFINE=	DOCS

do-install-DOCS-on:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_MAN} ${WRKSRC}/../README.md ${STAGEDIR}${DOCSDIR}

post-install:
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/xi-core

.include <bsd.port.mk>
