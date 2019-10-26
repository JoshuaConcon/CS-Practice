def addDomainVisitsToDict(domainName, visits, dictionary):
    if(domainName in dictionary):
        dictionary[domainName] += int(visits)
    else:
        dictionary[domainName] = int(visits)

def subdomainsFromCpDomain(cpDomain):
    subdomains = [cpDomain]
    while('.' in cpDomain):
        dotIndex = cpDomain.index('.')
        cpDomain = cpDomain[dotIndex+1:]
        subdomains.append(cpDomain)
    return subdomains

def getInfoFromCpdomainStr(cpdomainStr):
    split = cpdomainStr.split(' ')
    cpdomain = split[1]
    visits = split[0]
    return (cpdomain, visits)
    

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainsToVisits = {}
        for cpdomainStr in cpdomains:
            (cpdomain, visits) = getInfoFromCpdomainStr(cpdomainStr)
            subdomains = subdomainsFromCpDomain(cpdomain)
            for subdomain in subdomains:
                addDomainVisitsToDict(subdomain, visits, domainsToVisits)
        result = []
        for subdomain in domainsToVisits:
            subdomain_str = str(domainsToVisits[subdomain]) + ' ' + str(subdomain)
            result.append(subdomain_str)
        return result
        
            
