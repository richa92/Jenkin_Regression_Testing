#!/usr/bin/perl
use warnings;
use File::Copy;
$LOG="$0.log";

#die "usage: $0 <OA IP>" if @ARGV != 1;
die "usage: $0 <OA IP> <bay> <bay n>" if ((@ARGV < 2) || (@ARGV > 16));
$oa_ip=$ARGV[0];

@server_list=`ssh -l Administrator $oa_ip show server list`;
@server_list=grep(/[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/, @server_list);
foreach (@server_list) {
	@fields=split / /, $_;
	foreach $field (@fields) {
		if ($field =~ /^[0-9]{1,2}$/) {
			$bay=$field;
			if (grep (/^$bay$/,@ARGV)) {
				$server_info{$bay} = "Bond=yes"; 
			} else {
				$server_info{$bay} = "Bond=no"; 
			}
			#print "bay is $bay \n";
		}
		if ($field =~ /^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$/) {
			$ip=$field;
			$server_info{$bay} = join (" ", $ip, $server_info{$bay});
			#print "ip is $ip \n";
		}
	}
}

while ( ( $key, $value) = each %server_info ) {
	print "$key => $value\n"
}

foreach $key (sort {$a<=>$b} keys %server_info) {
	if (grep (/Bond=yes/, $server_info{$key})) {
		foreach ($server_info{$key}) {
			@fields=split / /, $_;
			foreach $field (@fields) {
				if ($field =~ /^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$/) {
					$iloip=$field;
					#make a system call
					system ("./connect-vsp-bond.exp $iloip 2>&1 | tee -a $LOG"); 
					#TODO: Need to check the return value of the system call so that we know
					# that the configuration succeeded.
				}
			}
		}
	}	
}
		
	 




	

