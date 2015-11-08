%global modname jdcal

Name:           python-%{modname}
Version:        1.0
Release:        1%{?dist}
Summary:        Julian dates from proleptic Gregorian and Julian calendars

# license file isn't included and requested during packaging
# https://github.com/phn/jdcal/issues/4
License:        BSD
URL:            https://github.com/phn/jdcal
Source0:        https://github.com/phn/jdcal/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
This module contains functions for converting between Julian dates and calendar
dates.

A function for converting Gregorian calendar dates to Julian dates, and another
function for converting Julian calendar dates to Julian dates are defined.
Two functions for the reverse calculations are also defined.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel

%description -n python2-%{modname}
This module contains functions for converting between Julian dates and calendar
dates.

A function for converting Gregorian calendar dates to Julian dates, and another
function for converting Julian calendar dates to Julian dates are defined.
Two functions for the reverse calculations are also defined.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel

%description -n python3-%{modname}
This module contains functions for converting between Julian dates and calendar
dates.

A function for converting Gregorian calendar dates to Julian dates, and another
function for converting Julian calendar dates to Julian dates are defined.
Two functions for the reverse calculations are also defined.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{modname}
%doc README.rst
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%doc README.rst
%{python3_sitelib}/%{modname}*
%{python3_sitelib}/__pycache__/%{modname}*

%changelog
* Sun Nov 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-1
- Initial package
