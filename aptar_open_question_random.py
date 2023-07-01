import os
import random

data = """
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/b7576a65-d888-4268-a075-b2baa779335f/?per_page=1&page=30
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/52d37b05-fc09-4149-8357-015cbe4c2053/?per_page=1&page=24
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/f552130a-6fd6-4e33-aa71-5cf45142b25e/?per_page=1&page=20
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/52bcbe12-adbe-4627-9d59-734b0bac8906/?per_page=1&page=20
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/8f62b668-002c-4482-a124-c1fada25e0fe/?per_page=1&page=20
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/1cbdffd5-99b0-478d-9c87-b5053e3579d5/?per_page=1&page=20
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/828ca874-681a-46c9-9c56-5790aa7b6807/?per_page=1&page=20
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/b77e7f48-4d71-4620-ad8b-03228deb78ed/?per_page=1&page=33
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/3ebf1ec9-8dfe-464d-a6d2-ce42a5463350/?per_page=1&page=41
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/f464c48e-ca6a-49f3-b4b7-58d153570d0c/?per_page=1&page=39
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/9bbba296-c50e-4971-995e-25b6cebec60d/?per_page=1&page=100
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/32f8b7bc-96fe-46c2-a26e-0ae647e70a8a/?per_page=1&page=14
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/583fb460-c806-4c65-93aa-1b064bcfa9fb/?per_page=1&page=30
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/ae33c33e-09b5-4628-92f3-2ed420d3527c/?per_page=1&page=21
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/ac5f68ff-484d-433d-b0c3-98265c00b1f6/?per_page=1&page=29
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/d0fb8616-716f-4dca-a004-46f5294b01a4/?per_page=1&page=60
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/cdf7b1c9-41a0-420d-a5dd-b83599207407/?per_page=1&page=25
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/121e021d-a5ae-4815-ab20-84ba12a8e37b/?per_page=1&page=70
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/4968f1e0-6f95-4586-a2d1-da26bb8fd189/?per_page=1&page=38
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/6f66a3b6-14e2-4f60-9ece-32580a45a227/?per_page=1&page=40
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/cae1453a-f252-4dd7-8500-4a6d4d2981f5/?per_page=1&page=20
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/fb8c4e2c-526d-4806-b299-655e7693bf9c/?per_page=1&page=30
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/8a0d4866-2b04-4682-a7fb-2d10b54b1b02/?per_page=1&page=30
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/6d9ee737-d09b-48e0-b64b-c7ab452db70f/?per_page=1&page=30
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/4dcf0240-1b35-4819-9d83-72b03e3646fc/?per_page=1&page=17
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/0c7665f3-c045-4595-aa4b-8985b742a37d/?per_page=1&page=22
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/bb982b9c-1b5c-4cd0-a911-c49bc9029bad/?per_page=1&page=20
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/722b0dda-9f97-4daa-9fa9-28a30c5ae061/?per_page=1&page=50
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/5143e3a7-1be3-4deb-8c21-a9e76bf41755/?per_page=1&page=20
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/48cc021c-0ec4-4bcf-bf84-ff1405d4edd0/?per_page=1&page=20
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/00f6e47f-e261-4e7d-af1c-1af27cf4e257/?per_page=1&page=20
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/cc212ae0-14f4-4e58-9c24-0dac306b0770/?per_page=1&page=50
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/d6b50679-9791-4d87-a66e-3fb72581864e/?per_page=1&page=30
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/639c3d4b-16c7-47d2-8a04-cd813ab59ec7/?per_page=1&page=32
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/63f95e6c-dab9-4fba-83dc-a09328cb2f0b/?per_page=1&page=50
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/a114c761-ef65-4023-a546-20a0225d53f8/?per_page=1&page=15
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/e39b21ad-30da-4654-b846-9fb9bf68b4c8/?per_page=1&page=22
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/ec22d6fb-20cd-4dec-b4d3-f2339a88f730/?per_page=1&page=50
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/fe3e9881-8572-403e-a84d-a363432a43c8/?per_page=1&page=37
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/5bf439ba-de76-41b9-a082-8216cd3a6428/?per_page=1&page=39
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/23079987-5cba-4d5e-ae39-86620702c6fc/?per_page=1&page=60
https://concursos.estrategia.com/cadernos-e-simulados/cadernos/8f2a1a71-165b-4dc7-9fe9-53911ccbdb09/?per_page=1&page=60
""".strip().splitlines()


target = data[random.randint(0, len(data) - 1)].replace("&", "^&")
equals = target.rfind("=")
base = target[:equals]
total = int(target[equals + 1:])
target = base + "=" + str(random.randint(1, total))
os.system("start " + target)
