class compiler::install {

      package { "build-essential":
      ensure => present
 }
     package { "binutils":
     ensure => present
  }
}

