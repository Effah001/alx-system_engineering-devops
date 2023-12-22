#kill a process
exec { 'pkillme':
  command => 'pkill pkillme',
}
