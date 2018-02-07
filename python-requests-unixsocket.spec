# Created by pyp2rpm-3.2.3
%global pypi_name requests-unixsocket

Name:           python-%{pypi_name}
Version:        0.1.5
Release:        2%{?dist}
Summary:        Use requests to talk HTTP via a UNIX domain socket

License:        Apache-2
URL:            https://github.com/msabramo/requests-unixsocket
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pbr
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
requests-unixsocket Use requests < to talk HTTP via a UNIX domain
socketUsage++++++++You can use it by instantiating a special Session object:..
code-block:: python import requests_unixsocket session
requests_unixsocket.Session() Access /path/to/page from /tmp/profilesvc.sock

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-requests >= 1.1
Requires:       python-urllib3 >= 1.8
%description -n python2-%{pypi_name}
requests-unixsocket Use requests < to talk HTTP via a UNIX domain
socketUsage++++++++You can use it by instantiating a special Session object:..
code-block:: python import requests_unixsocket session
requests_unixsocket.Session() Access /path/to/page from /tmp/profilesvc.sock

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-requests >= 1.1
Requires:       python%{python3_pkgversion}-urllib3 >= 1.8
%description -n python%{python3_pkgversion}-%{pypi_name}
requests-unixsocket Use requests < to talk HTTP via a UNIX domain
socketUsage++++++++You can use it by instantiating a special Session object:..
code-block:: python import requests_unixsocket session
requests_unixsocket.Session() Access /path/to/page from /tmp/profilesvc.sock


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install

%py2_install


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/requests_unixsocket
%{python2_sitelib}/requests_unixsocket-%{version}-py?.?.egg-info

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/requests_unixsocket
%{python3_sitelib}/requests_unixsocket-%{version}-py?.?.egg-info

%changelog
* Tue Feb 06 2018 Brian J. Murrell <brian.murrell@intel.com> - 0.1.5-2
- Need to override pyp2rpm's Requires: python2-urllib3 >= 1.8 as
  urllib3 has not been migrated to python{2,3} yet.

* Wed Jan 24 2018 Brian J. Murrell <brian.murrell@intel.com> - 0.1.5-1
- Initial package.
