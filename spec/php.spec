Summary: PHP 7 - A powerful scripting language
Name: php
Version: 7
Release: 1
Group: Networking/Daemons
Source0: php-src-master.tar.gz
License: BSD
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: zookeeper-native, libcurl-devel, openssl, pcre, readline, libmcrypt, libcurl

%description
PHP 7 is a powerful apache module that adds scripting and database connection
capabilities to the apache server. This version includes the "php_cgi" binary
for suExec and stand alone php scripts too.

%prep
%setup -q -n php-src-master
#mkdir manual; cd manual && tar xzf $RPM_SOURCE_DIR/php3-manual.tar.gz
./buildconf

%build
# first the standalone (why can't you build both at once?)
# need to run this under sh or it breaks

sh ./configure --prefix=/opt/php \
	--with-config-file-path=%{_sysconfdir} \
	--enable-force-cgi-redirect \
	--enable-safe-mode \
	--with-exec-dir=/opt/php/bin \
	--with-mysql \
	--with-zlib \
	--enable-xml \
	--enable-wddx \
	--with-gd \
	--enable-shared \
	--with-mysql=mysqlnd \
        --with-mysqli=mysqlnd \
        --with-pdo-mysql=mysqlnd \
        --with-iconv \
        --enable-xml \
        --enable-bcmath \
        --enable-shmop \
        --enable-sysvsem \
        --enable-inline-optimization \
        --enable-mbregex \
        --enable-fpm \
        --enable-mbstring \
        --enable-gd-native-ttf \
        --with-openssl \
        --enable-pcntl \
        --enable-sockets \
        --with-xmlrpc \
        --enable-zip \
        --enable-soap \
        --with-gettext \
        --enable-session \
        --with-curl \
        --with-jpeg-dir \
        --with-freetype-dir \
        --with-fpm-user=nobody \
	--with-fpm-group=nobody \
	--enable-exif \
	--enable-opcache 
make
make install
%install
rm -rf $RPM_BUILD_ROOT
#mkdir -p $RPM_BUILD_ROOT%{_libdir}/apache
#install -m 0755 .libs/libphp7.so $RPM_BUILD_ROOT%{_libdir}/apache
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 sapi/cli/php $RPM_BUILD_ROOT%{_bindir}/php
install -m 0755 sapi/cgi/php-cgi $RPM_BUILD_ROOT%{_bindir}/php-cgi
install -m 0755 sapi/fpm/php-fpm $RPM_BUILD_ROOT%{_bindir}/php-fpm
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
install -m 0755 sapi/fpm/init.d.php-fpm $RPM_BUILD_ROOT%{_sbindir}/php-fpm
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -m 0755 php.ini-production $RPM_BUILD_ROOT%{_sysconfdir}/php.ini
install -m 0755 sapi/fpm/php-fpm.conf $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.conf
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d
install -m 0755 sapi/fpm/www.conf $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d/www.conf
mkdir -p $RPM_BUILD_ROOT%{_libdir}/php/extensions
install -m 0755 modules/*.so $RPM_BUILD_ROOT%{_libdir}/php/extensions

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Nov 27 2003 Marcus Boerger <helly@php.net>
- Fix requirements for older systems.
- Fix rpm build directory for the major distributions.
- Fix config dir.
- Rename package to php.
- Add gd extension.
- Support building of shared extensions.
- Build CLI only once.

* Fri Oct 31 2003 Marcus Boerger <helly@php.net>
- Update version to 5.
- Remove unsure external requirements.
- Remove non existing directories
- Fix targets.
- Install both CLI and CGI.
- Install manpage.
- Install ini.

* Mon Mar 04 2002 Arjen Lentz <agl@bitbike.com>
- Fix path and remove --with-imap due to conflicts with kerberos.

* Fri Jun 29 2001 Jani Taskinen <sniper@iki.fi>
- Removed some useless configure options. Made the tar names correct.

* Sun Apr 30 2000 Joey Smith <joey@samaritan.com>
- Small fix: Description still referred to package as PHP3.

* Wed Jul 21 1999 Sam Liddicott <sam@campbellsci.co.uk>
- added php4b1 and modified cgi building rules so it doesn't break module

* Wed Mar 17 1999 Sam Liddicott <sam@campbellsci.co.uk>
- Stuffed in 3.0.7 source tar and added "php" as a build destination

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- rebuild for apache 1.3.3

* Thu Oct 08 1998 Preston Brown <pbrown@redhat.com>
- updated to 3.0.5, fixes nasty bugs in 3.0.4.

* Sun Sep 27 1998 Cristian Gafton <gafton@redhat.com>
- updated to 3.0.4 and recompiled for apache 1.3.2

* Thu Sep 03 1998 Preston Brown <pbrown@redhat.com>
- improvements; builds with apache-devel package installed.

* Tue Sep 01 1998 Preston Brown <pbrown@redhat.com>
- Made initial cut for PHP3.

%files
%defattr(-,nobody,nobody)
%{_bindir}/php*
%{_bindir}/php*
%{_sysconfdir}/php.ini
%{_sysconfdir}/php-fpm.conf
%{_sysconfdir}/php-fpm.d/*
%{_libdir}/php/extensions/*.so

