class users::configure  {
  File {
   require => Class["passhash::install"],
}

  group { 'developers':
    ensure => present,
    gid => 1111,
  }

  user { 'janet':
    ensure => 'present',
    comment => 'project-1',
    groups => ['sudo','developers'],
    home => '/home/janet',
    password_max_age => '99999',
    password => '$6$FHcMzrQE/e9Wy$etPJnCNmI5reTHOpxzoR0u1iZ.xox9prG0Pe3imulRxTbR1bGw2qI9EuA1sIp1vZdo/0183vSxNwbpHbqcFiR1',
    password_min_age => '0',
    shell => '/bin/bash',
    uid => '1001',
    require => Group['developers'],
  }

  user { 'tim':
    ensure => 'present',
    comment => 'project-1',
    groups => ['sudo', 'developers'],
    home => '/home/tim',
    password => '$6$FHcMzrQE/e9Wy$etPJnCNmI5reTHOpxzoR0u1iZ.xox9prG0Pe3imulRxTbR1bGw2qI9EuA1sIp1vZdo/0183vSxNwbpHbqcFiR1',
    password_max_age => '99999',
    password_min_age => '0',
    shell => '/bin/bash',
    uid => '1002',
    require => Group['developers'],

  }

  user { 'bob':
    ensure => 'present',
    comment => 'project-1',
    groups => ['sudo'],
    home => '/home/bob',
    password => '$6$FHcMzrQE/e9Wy$etPJnCNmI5reTHOpxzoR0u1iZ.xox9prG0Pe3imulRxTbR1bGw2qI9EuA1sIp1vZdo/0183vSxNwbpHbqcFiR1',
    password_max_age => '99999',
    password_min_age => '0',
    shell => '/bin/bash',
    uid => '1003'
  }

  user { 'alice':
    ensure => 'present',
    comment => 'project-1',
    groups => ['sudo'],
    home => '/home/alice',
    password => '$6$FHcMzrQE/e9Wy$etPJnCNmI5reTHOpxzoR0u1iZ.xox9prG0Pe3imulRxTbR1bGw2qI9EuA1sIp1vZdo/0183vSxNwbpHbqcFiR1',
    password_max_age => '99999',
    password_min_age => '0',
    shell => '/bin/bash',
    uid => '1004',
  }
}
