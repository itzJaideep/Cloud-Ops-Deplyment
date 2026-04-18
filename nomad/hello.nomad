job "cloudops-app" {
  datacenters = ["dc1"]

  group "app" {
    task "web" {
      driver = "docker"

      config {
        image = "cloudops-app"
        ports = ["http"]
      }

      resources {
        cpu    = 500
        memory = 256
      }

      network {
        port "http" {
          static = 5000
        }
      }
    }
  }
}
