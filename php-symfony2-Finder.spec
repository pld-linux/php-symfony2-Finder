# $Revision: 1.31 $, $Date: 2011/04/10 20:45:35 $
%define		status		stable
%define		pearname	Finder
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Symfony2 Finder Component
Name:		php-symfony2-Finder
Version:	2.1.6
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	0207418a1f86fe8f10b31aaef20e0317
URL:		http://pear.symfony.com/package/Finder/
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 1.3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Symfony2 Finder Component

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

# no packaging of tests
rm -r .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests
rm .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist
rm .%{php_pear_dir}/Symfony/Component/Finder/.gitattributes

# fixups
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/CHANGELOG.md .
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/Finder
%{php_pear_dir}/Symfony/Component/Finder/*.php
%{php_pear_dir}/Symfony/Component/Finder/Comparator
%{php_pear_dir}/Symfony/Component/Finder/Iterator
