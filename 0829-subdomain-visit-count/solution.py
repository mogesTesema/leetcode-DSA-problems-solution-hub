class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        domain_count = {}


        def parse_domain(pair_domain):
            domains_pair = pair_domain.split(" ")
            count = int(domains_pair[0])
            domains = domains_pair[1]
            domains = domains.split(".")[::-1]
            parent_domain = ""
            for domain in domains:
                if len(parent_domain) == 0:
                    domain += parent_domain
                else:
                    domain += "."+ parent_domain
                parent_domain = domain
                if domain in domain_count:
                    domain_count[domain] += count
                else:
                    domain_count[domain] = count
    

        for cpdomain in cpdomains:
            parse_domain(cpdomain)

    
        ans = []

        for key,val in domain_count.items():
            coupled = str(val) + " " + key
            ans.append(coupled)
        return ans

    

            

        
        
        

