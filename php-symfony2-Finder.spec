%define		package	Finder
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Finder Component
Name:		php-symfony2-Finder
Version:	2.7.3
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	e04c6298dc9b422114acef9e7f6bc2da
URL:		http://symfony.com/doc/2.7/components/finder.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-pear >= 1.3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Finder Component finds files and directories via an intuitive
fluent interface.

%prep
%setup -q -n %{package}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/Finder
%{php_pear_dir}/Symfony/Component/Finder/*.php
%{php_pear_dir}/Symfony/Component/Finder/Adapter
%{php_pear_dir}/Symfony/Component/Finder/Comparator
%{php_pear_dir}/Symfony/Component/Finder/Exception
%{php_pear_dir}/Symfony/Component/Finder/Expression
%{php_pear_dir}/Symfony/Component/Finder/Iterator
%{php_pear_dir}/Symfony/Component/Finder/Shell
