        def check_register(input_string):
        #remove the pass and write your logic here
        #pass
        output_string = 'X'
        if(len(input_string)%4==0):
            output_string='A'
        if('KA' or 'ka' in input_string):
            x=list(input_string)
            count = 0
            for i in range(0, len(x)):

                if((x[i]=='K' or x[i]=='k') and (x[i+1] == 'A' or x[i+1]=='a')):
                    count=count+1
            if(count==1):
                   output_string='B'
        if('-' in input_string):
            x=list(input_string)
            count =0
            for i in range(0,len(x)):
                if(x[i]=='-'):
                    count=count+1
            if(count==2):
                output_string='C'
        y=list(input_string)
        if( y[3]=='0'):
            output_string='D'
        co=0
        for i in y:
            if(i in "0123456789"):
                co+=int(i)

        if(co>12):
            output_string='E'

        return output_string

#function_2
#You can change the values in the below code and check for manual testing
#input_string="RJ-80EK1122"
#check_register(input_string);
~
~
