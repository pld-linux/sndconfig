Name: sndconfig
Version: 0.33
Release: 1
Copyright: GPL
Summary: The Red Hat Linux sound configuration tool.
Group: Applications/Multimedia
Source: sndconfig-%{PACKAGE_VERSION}.tar.gz
%ifarch i386 alpha
Requires: isapnptools >= 1.16, sox, awesfx, playmidi, kernel >= 2.2.0
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch: i386 sparc alpha

%description
Sndconfig is a text based tool which sets up the configuration
files you'll need to use a sound card with a Red Hat Linux system.
Sndconfig can be used to set the proper sound type for programs
which use the /dev/dsp, /dev/audio and /dev/mixer devices.  The
sound settings are saved by the aumix and sysV runlevel scripts.

Install sndconfig if you need to configure your sound card.

%prep
%setup -n sndconfig

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{sbin,man/man8}
mkdir -p $RPM_BUILD_ROOT/usr/share/locale
make prefix=$RPM_BUILD_ROOT/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
/usr/sbin/sndconfig
%ifarch i386 alpha
/usr/sbin/pnpprobe
/usr/man/man8/pnpprobe.8
%endif
/usr/share/sndconfig/sample.au
/usr/share/sndconfig/sample.midi
/usr/share/locale/*/*/sndconfig.mo
/usr/man/man8/sndconfig.8
