#!/usr/bin/perl
use warnings;
use File::Copy;
$LOG="$0.log";

die "usage: $0 <OA IP> <ipaddr.conf> <server.conf>" if @ARGV != 3;
$oa_ip=$ARGV[0];
$fileIpaddr=$ARGV[1];
$fileServer=$ARGV[2];

if (-e $fileServer) {
	@ext=map { ("a".."z")[rand 26] } 1..8;
	$extention=join "", @ext;
	move($fileServer, $fileServer.$extention);
}

open(FH, $fileIpaddr,) or die ("Unable to open $fileIpaddr"); 
@ipaddr = <FH>;
foreach (@ipaddr) {
	@line=split / /, $_;
	foreach $field (@line) {
		if ($field =~ /\:[1-9]{1}$/) {
			@profile_port=split /:/, $field; 
			foreach (@profile_port) {
				if ($_ =~ /^[0-9]{1,3}$/) {
					$port=$_;
					#print "port is $port\n";
				}
				if ($_ =~/^[A-Za-z]/) {
					$profile=$_;
					#print "profile is $profile\n";
					@profile_bay=split /_/, $profile;
					foreach (@profile_bay) {
						if ($_ =~ /^[0-9]{1,2}$/) {
							$bay=$_;
							if ($bay =~ /^0/) {
								$bay =~ s/^0//;
								$bay = sprintf("%- 1s", $bay);
				#				print "bay is $bay\n"
							}
						}
					}
				}
			}
		}
		if ($field =~ /^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$/) {
			$ip=$field;
		}
		if ($field =~ /^[0-9]{1,4}$/) {
			$vlan=$field;
		}
		if ($field =~ /^([0-9a-fA-F]{2}([:]|$)){6}$/) {
			$mac=$field;
		}
	}	
	$profile_ip = join " " , $profile, $ip, $mac, $vlan;
	if (!(exists $server_conf{$bay})) {
		$server_conf{$bay} = $profile_ip;
	}
}
close(FH);

@server_list=`ssh -l Administrator $oa_ip show server list`;
@server_list=grep(/[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/, @server_list);
foreach (@server_list) {
	@fields=split / /, $_;
	foreach $field (@fields) {
		if ($field =~ /^[0-9]{1,2}$/) {
			$bay=$field;
		#	print "bay is $bay \n";
		}
		if ($field =~ /^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$/) {
			$ip=$field;
		#	print "ip is $ip \n";
		}
		$server_info{$bay} = $ip;
	}
}

#while ( ( $key, $value) = each %server_info ) {
#	print "$key => $value\n"
#}

open(FH, "+>", $fileServer); 
select((select(FH), $|=1)[0]);
foreach $key (sort {$a<=>$b} keys %server_conf) {
#	print "$key => $server_conf{$key}\n";

	# Turn off the buffering by making the file handle hot
	#{ $fileServer = select FH;
	#  $| = 1;
	#  select $fileServer;
	#}
	foreach ($server_conf{$key}) {
		@fields=split / /, $_;
		foreach $field (@fields) {
			if ($field =~ /^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$/) {
				$ip=$field;
			}
			if ($field =~ /^[0-9]{1,4}$/) {
				$vlan=$field;
			}	
			if ($field =~ /^([0-9a-fA-F]{2}([:]|$)){6}$/) {
				$mac=$field;
			}
			if ($field =~ /^[A-Za-z]/) {
				$profile=$field;
			}
		}
	#make a system call
	$iloip=$server_info{$key};
	#print "ip is $ip, ,iloip is $iloip,  mac is $mac, vlan is $vlan\n";
	system ("./connect-vsp.exp $iloip $mac $vlan $ip 2>&1 | tee -a $LOG"); 
	#TODO: Need to check the return value of the system call so that we know
	# that the configuration succeeded.
	print FH "$profile=$ip";
	print "$profile=$ip";
	}
}
close(FH);
		
	 




	

