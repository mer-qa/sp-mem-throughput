Name: sp-mem-throughput
Version: 0.4.4
Release: 0
Summary: Memory throughput testing tool
License: GPLv2+
URL: https://github.com/mer-qa/sp-mem-throughput
Source: %{name}-%{version}.tar.gz
%ifarch %{arm}
BuildRequires: python3-base
%endif

%description
 This is a tool for benchmarking memory throughput by different access
 patterns, such as read only, write only (similar to the memset function from
 the C library), or copy (similar to memcpy from the C library). For each of
 these access patterns, various implementations can be benchmarked, including
 those found in the C library.
 .
 sp-mem-throughput has various parameters, that can be set to measure different
 kind of workloads, for example to measure the memory throughput when writing
 to very small or very large memory areas.
 .
 Results can be stored in CSV format for later analysis.
 
%prep
%setup -q

%build
%make_build

%install
%make_install

%files
%{_bindir}/sp-mem-throughput
%{_mandir}/man1/sp-mem-throughput.1.gz
%doc COPYING 
