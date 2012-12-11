# $Revision: 1.31 $, $Date: 2011/04/10 20:45:35 $
%define		status		stable
%define		pearname	Finder
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Symfony2 Finder Component
Name:		php-symfony2-Finder
Version:	2.1.2
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	aab0c7d376dd9c6371b07f29a25a2e41
URL:		http://pear.symfony.com/package/Finder/
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Symfony2 Finder Component

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

# no packaging of tests
rm -r .%{php_pear_dir}/Symfony/Component/Finder/Tests
rm .%{php_pear_dir}/Symfony/Component/Finder/phpunit.xml.dist

# fixups
mv .%{php_pear_dir}/Symfony/Component/Finder/CHANGELOG.md .
mv docs/Finder/Symfony/Component/Finder/* .

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
# XXX proper dirs
%dir %{php_pear_dir}/Symfony
%dir %{php_pear_dir}/Symfony/Component
%dir %{php_pear_dir}/Symfony/Component/Finder
%{php_pear_dir}/Symfony/Component/Finder/*.php
%{php_pear_dir}/Symfony/Component/Finder/Comparator
%{php_pear_dir}/Symfony/Component/Finder/Iterator
