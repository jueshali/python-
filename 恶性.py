i = 0
j = 0
flag = 0
s = 0
nums1 = [1,4]
nums2 = [3]

if nums1 == []:
    if len(nums2)%2==1:  
        s =  nums2[len(nums2)/2];  
    else:  
        s= (nums2[len(nums2)/2-1]+nums2[len(nums2)/2])/2.0;
if nums2 == []:
    if len(nums1)%2==1:  
        s= nums1[len(nums1)/2];  
    else:  
        s= (nums1[len(nums1)/2-1]+nums1[len(nums1)/2])/2.0;
        
            
else:
    while (i + j) < ((len(nums1)+len(nums2))/2-1) and i < len(nums1)-1 and j < len(nums2)-1:
        if nums1[i] < nums2[j] :
            i = i + 1
        
        else:
            j = j + 1
            
              
    if (len(nums1) + len(nums2)) % 2 == 0:
        if i == len(nums1)-1:
            while (i + j) < ((len(nums1)+len(nums2))/2-1):
                nums1[i] = max(nums1[i],nums2[j])
                j = j+1
        if j == len(nums2)-1:
            while (i + j) < ((len(nums1)+len(nums2))/2-1):
                nums2[j] = max(nums1[i],nums2[j])
                i = i+1
        s= float(nums1[i] + nums2[j])/2
    else:
        if i == len(nums1)-1:
            while (i + j) < ((len(nums1)+len(nums2))/2-1):
                nums1[i] = max(nums1[i],nums2[j])
                j = j+1
        if j == len(nums2)-1:
            while (i + j) < ((len(nums1)+len(nums2))/2-1):
                nums2[j] = max(nums1[i],nums2[j])
                i = i+1
        s= float(max(nums1[i],nums2[j]))
        
