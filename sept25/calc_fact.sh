calc_fact(){
        num=$1
        fac=1
        while [ $num -gt 1 ]
        do
                fac=$((fac*num))
                num=$(( num-1))
        done
        return $fac

}
read -p "Num : " num
calc_fact $num
echo $?
