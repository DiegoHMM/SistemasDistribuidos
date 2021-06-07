ClientConfiguration cfg = new ClientConfiguration().setAddresses("34.72.162.100:10800");
IgniteClient client = Ignition.startClient(cfg);

ClientCache<Integer, String> cache = client.getOrCreateCache("test_cache");

cache.put(1, "first test value");

System.out.println(cache.get(1));

client.close();