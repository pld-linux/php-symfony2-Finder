%define		package	Finder
%define		php_min_version 5.3.9
Summary:	Symfony2 Finder Component
Name:		php-symfony2-Finder
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	e77d0f7fdd7a5be8b1a0ad9a8c9a965b
URL:		http://symfony.com/doc/2.7/components/finder.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Finder Component finds files and directories via an intuitive
fluent interface.

%prep
%setup -q -n finder-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/Finder
%{php_data_dir}/Symfony/Component/Finder/*.php
%{php_data_dir}/Symfony/Component/Finder/Adapter
%{php_data_dir}/Symfony/Component/Finder/Comparator
%{php_data_dir}/Symfony/Component/Finder/Exception
%{php_data_dir}/Symfony/Component/Finder/Expression
%{php_data_dir}/Symfony/Component/Finder/Iterator
%{php_data_dir}/Symfony/Component/Finder/Shell
