Summary:            A fast, distributed, high performance gradient boosting (GBDT, GBRT, GBM or MART) framework based on decision tree algorithms
Name:               LightGBM
Version:            2.2.2
Release:            1%{?dist}
License:            ASL 2.0
Group:              System Environment/Base
Source:             %{name}-%{version}.tar.gz
URL:                https://github.com/Microsoft/LightGBM

%description
A fast, distributed, high performance gradient boosting (GBDT, GBRT, GBM or MART) framework based on decision tree algorithms, used for ranking, classification and many other machine learning tasks. It is under the umbrella of the DMTK(http://github.com/microsoft/dmtk) project of Microsoft.

%prep
%setup

%build
mkdir build
cd build
cmake ..  -DCMAKE_INSTALL_PREFIX=/usr
make -j32

%install
%{__mkdir} -p %{buildroot}/%{_bindir}
%{__mkdir} -p %{buildroot}%{_libdir}
%{__mkdir} -p %{buildroot}%{_includedir}

%{__cp} -rp %{_builddir}/%{name}-%{version}/lib_lightgbm.so %{buildroot}%{_libdir}
%{__cp} -rp %{_builddir}/%{name}-%{version}/lightgbm %{buildroot}%{_bindir}
%{__cp} -rp %{_builddir}/%{name}-%{version}/include/LightGBM %{buildroot}%{_includedir}

%files
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*

