param="$(pyro4-nsc -n localhost -p 50001 list)"

python3 set_fs_id.py "'$param'"

