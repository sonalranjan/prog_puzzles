function solution(time) {
    let hhmm = time.split(":")
    if (hhmm.length != 2) {
        return false
    }
    switch(hhmm[0][0]) {
        case "0":
        case "1":
            if (! "0123456789".includes(hhmm[0][1])) {
                return false
            }
            break;
        case "2":
            if (! "0123".includes(hhmm[0][1])) {
                return false
            }
            break;
    }
    
    if (! "012345".includes(hhmm[1][0])) {
        return false
    }
    if (! "0123456789".includes(hhmm[1][1])) {
        return false
    }
    // console.log(validHrs)
    return true; 
}

