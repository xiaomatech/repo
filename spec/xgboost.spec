Summary:            Large-scale and Distributed Gradient Boosting (GBDT, GBRT or GBM) Library
Name:               xgboost
Version:            0.81
Release:            1%{?dist}
License:            ASL 2.0
Group:              System Environment/Base
Source:             %{name}-%{version}.tar.gz
URL:                https://github.com/dmlc/xgboost
Requires:           openmpi
BuildRequires:      cmake3
BuildRequires:      openmpi-devel

%description
Scalable, Portable and Distributed Gradient Boosting (GBDT, GBRT or GBM) Library, for Python, R, Java, Scala, C++ and more. Runs on single machine, Hadoop, Spark, Flink and DataFlow

%prep
%setup

%build
mkdir build
cd build
cmake3 .. -DUSE_CUDA=ON -DUSE_NCCL=ON -DUSE_OPENMP=ON
cd ../
make -j32
make all
make jvm

%install
%{__mkdir} -p %{buildroot}/%{_bindir}
%{__mkdir} -p %{buildroot}%{_libdir}
%{__mkdir} -p %{buildroot}%{_includedir}

%{__cp} -rp %{_builddir}/%{name}-%{version}/dmlc-core/libdmlc.a %{buildroot}%{_libdir}
%{__cp} -rp %{_builddir}/%{name}-%{version}/rabit/lib/librabit.a %{buildroot}%{_libdir}
%{__cp} -rp %{_builddir}/%{name}-%{version}/lib/libxgboost.a %{buildroot}%{_libdir}
%{__cp} -rp %{_builddir}/%{name}-%{version}/jvm-packages/lib/libxgboost4j.so %{buildroot}%{_libdir}
%{__cp} -rp %{_builddir}/%{name}-%{version}/lib/libxgboost.so %{buildroot}%{_libdir}
%{__cp} -rp %{_builddir}/%{name}-%{version}/xgboost %{buildroot}%{_bindir}

%{__cp} -rp %{_builddir}/%{name}-%{version}/dmlc-core/include/dmlc %{buildroot}%{_includedir}
%{__cp} -rp %{_builddir}/%{name}-%{version}/include/xgboost %{buildroot}%{_includedir}

%files
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*

