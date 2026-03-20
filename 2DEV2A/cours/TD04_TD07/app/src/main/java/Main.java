import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import com.google.gson.Gson;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.US);

        // =========================
        // Défi 4 :
        // Initialisation des données en mémoire de l'application
        // - AddressBook : ensemble d'adresses connues
        // - TripRepository : collection des trajets publiés
        // - RouteService : service qui calcule l'itinéraire via l'API
        // =========================
        AddressBook addressBook = new AddressBook();
        TripRepository tripRepository = new TripRepository();
        RouteService routeService = new RouteService("86c0f8db-0c73-4fb8-8e83-c1e9c23dd743"); // Remplace par ta vraie clé

        CarpoolApp app = new CarpoolApp(scanner, addressBook, tripRepository, routeService);
        app.start();
    }
}

/* =========================
   APPLICATION
   ========================= */

class CarpoolApp {
    private final Scanner scanner;
    private final AddressBook addressBook;
    private final TripRepository tripRepository;
    private final RouteService routeService;

    public CarpoolApp(Scanner scanner, AddressBook addressBook, TripRepository tripRepository, RouteService routeService) {
        this.scanner = scanner;
        this.addressBook = addressBook;
        this.tripRepository = tripRepository;
        this.routeService = routeService;
    }

    public void start() {
        System.out.println("==================================");
        System.out.println("Bienvenue dans l'application de covoiturage");
        System.out.println("==================================");

        boolean running = true;

        while (running) {
            System.out.println("\nMenu :");
            System.out.println("1. Publier un trajet");
            System.out.println("2. Rechercher un trajet");
            System.out.println("3. Afficher tous les trajets");
            System.out.println("0. Quitter");
            System.out.print("Votre choix : ");

            int choice = readInt();

            switch (choice) {
                case 1:
                    // Défi 5 : publier un trajet
                    publishTrip();
                    break;
                case 2:
                    // Défi 6 : rechercher un trajet
                    searchTrips();
                    break;
                case 3:
                    displayAllTrips();
                    break;
                case 0:
                    running = false;
                    System.out.println("Au revoir !");
                    break;
                default:
                    System.out.println("Choix invalide.");
            }
        }
    }

    private void publishTrip() {
        System.out.println("\n=== Publication d'un trajet ===");

        // =========================
        // Défi 5 - étape 1 :
        // demander à l'utilisateur les informations du trajet
        // ici on lui demande :
        // - la ville de départ
        // - la ville d'arrivée
        // - le nombre de places disponibles
        // =========================
        Address departure = chooseAddress("Choisissez la ville de départ");
        Address destination = chooseAddress("Choisissez la ville d'arrivée");

        if (departure.equals(destination)) {
            System.out.println("Le départ et l'arrivée doivent être différents.");
            return;
        }

        System.out.print("Nombre de places disponibles : ");
        int availableSeats = readInt();

        if (availableSeats <= 0) {
            System.out.println("Le nombre de places doit être supérieur à 0.");
            return;
        }

        try {
            // =========================
            // Défi 5 - étape 2 :
            // calculer l'itinéraire correspondant
            // grâce au service RouteService qui interroge GraphHopper
            // =========================
            RouteInfo routeInfo = routeService.calculateRoute(departure, destination);

            // =========================
            // Défi 5 - étape 3 :
            // créer le trajet avec les informations saisies
            // et les données calculées (distance + durée)
            // =========================
            Trip trip = new Trip(departure, destination, availableSeats, routeInfo.distanceMeters, routeInfo.durationMs);

            // =========================
            // Défi 5 - étape 4 :
            // stocker le trajet en mémoire
            // =========================
            tripRepository.addTrip(trip);

            System.out.println("\nTrajet publié avec succès.");
            System.out.println(trip);
        } catch (IOException e) {
            System.out.println("Erreur lors du calcul de l'itinéraire : " + e.getMessage());
        }
    }

    private void searchTrips() {
        System.out.println("\n=== Recherche de trajets ===");

        // =========================
        // Défi 6 - étape 1 :
        // demander à l'utilisateur son point de départ
        // et sa destination
        // =========================
        Address departure = chooseAddress("Choisissez la ville de départ");
        Address destination = chooseAddress("Choisissez la ville d'arrivée");

        // =========================
        // Défi 6 - étape 2 :
        // récupérer les trajets qui correspondent
        // à ces critères
        // =========================
        List<Trip> results = tripRepository.searchTrips(departure, destination);

        // =========================
        // Défi 6 - étape 3 :
        // afficher les trajets trouvés
        // =========================
        if (results.isEmpty()) {
            System.out.println("Aucun trajet trouvé pour " + departure.getName() + " -> " + destination.getName());
            return;
        }

        System.out.println("\nTrajets trouvés :");
        for (int i = 0; i < results.size(); i++) {
            System.out.println((i + 1) + ". " + results.get(i));
        }
    }

    private void displayAllTrips() {
        System.out.println("\n=== Tous les trajets publiés ===");

        List<Trip> allTrips = tripRepository.getAllTrips();

        if (allTrips.isEmpty()) {
            System.out.println("Aucun trajet publié.");
            return;
        }

        for (int i = 0; i < allTrips.size(); i++) {
            System.out.println((i + 1) + ". " + allTrips.get(i));
        }
    }

    private Address chooseAddress(String message) {
        System.out.println("\n" + message + " :");

        // =========================
        // Défi 4 :
        // on utilise ici la liste des adresses connues,
        // déjà chargées en mémoire dans AddressBook
        // pour éviter de les recharger à chaque demande
        // =========================
        List<Address> addresses = addressBook.getKnownAddresses();

        for (int i = 0; i < addresses.size(); i++) {
            System.out.println((i + 1) + ". " + addresses.get(i).getName());
        }

        int choice;
        do {
            System.out.print("Votre choix : ");
            choice = readInt();
        } while (choice < 1 || choice > addresses.size());

        return addresses.get(choice - 1);
    }

    private int readInt() {
        while (!scanner.hasNextInt()) {
            System.out.print("Veuillez entrer un nombre valide : ");
            scanner.next();
        }
        return scanner.nextInt();
    }
}

/* =========================
   MODELE
   ========================= */

class Address {
    private final String name;
    private final double latitude;
    private final double longitude;

    public Address(String name, double latitude, double longitude) {
        this.name = name;
        this.latitude = latitude;
        this.longitude = longitude;
    }

    public String getName() {
        return name;
    }

    public double getLatitude() {
        return latitude;
    }

    public double getLongitude() {
        return longitude;
    }

    @Override
    public String toString() {
        return name + " (" + latitude + ", " + longitude + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Address)) return false;
        Address other = (Address) obj;
        return this.name.equalsIgnoreCase(other.name);
    }

    @Override
    public int hashCode() {
        return name.toLowerCase().hashCode();
    }
}

class Trip {
    // =========================
    // Défi 4 :
    // définition de ce qu'est un trajet
    // un trajet contient :
    // - un point de départ
    // - une destination
    // - un nombre de places
    // ici on ajoute aussi :
    // - la distance
    // - la durée
    // =========================
    private final Address departure;
    private final Address destination;
    private final int availableSeats;
    private final double distanceMeters;
    private final long durationMs;

    public Trip(Address departure, Address destination, int availableSeats, double distanceMeters, long durationMs) {
        this.departure = departure;
        this.destination = destination;
        this.availableSeats = availableSeats;
        this.distanceMeters = distanceMeters;
        this.durationMs = durationMs;
    }

    public Address getDeparture() {
        return departure;
    }

    public Address getDestination() {
        return destination;
    }

    public int getAvailableSeats() {
        return availableSeats;
    }

    public double getDistanceMeters() {
        return distanceMeters;
    }

    public long getDurationMs() {
        return durationMs;
    }

    @Override
    public String toString() {
        double distanceKm = distanceMeters / 1000.0;
        long durationMinutes = durationMs / 1000 / 60;

        return departure.getName() + " -> " + destination.getName()
                + " | places: " + availableSeats
                + " | distance: " + String.format(Locale.US, "%.2f km", distanceKm)
                + " | durée: " + durationMinutes + " min";
    }
}

/* =========================
   DONNEES EN MEMOIRE
   ========================= */

class AddressBook {
    // =========================
    // Défi 4 :
    // ensemble d'adresses connues,
    // stockées en mémoire avec leurs coordonnées
    // =========================
    private final List<Address> knownAddresses = new ArrayList<>();

    public AddressBook() {
        knownAddresses.add(new Address("Paris", 48.8566, 2.3522));
        knownAddresses.add(new Address("Lyon", 45.7640, 4.8357));
        knownAddresses.add(new Address("Marseille", 43.2965, 5.3698));
        knownAddresses.add(new Address("Lille", 50.6292, 3.0573));
        knownAddresses.add(new Address("Bordeaux", 44.8378, -0.5792));
        knownAddresses.add(new Address("Toulouse", 43.6047, 1.4442));
        knownAddresses.add(new Address("Nantes", 47.2184, -1.5536));
        knownAddresses.add(new Address("Strasbourg", 48.5734, 7.7521));
    }

    public List<Address> getKnownAddresses() {
        return knownAddresses;
    }
}

class TripRepository {
    // =========================
    // Défi 4 :
    // collection des trajets publiés,
    // gardée en mémoire pendant l'exécution
    // =========================
    private final List<Trip> trips = new ArrayList<>();

    public void addTrip(Trip trip) {
        trips.add(trip);
    }

    public List<Trip> getAllTrips() {
        return trips;
    }

    public List<Trip> searchTrips(Address departure, Address destination) {
        List<Trip> results = new ArrayList<>();

        for (Trip trip : trips) {
            if (trip.getDeparture().equals(departure) && trip.getDestination().equals(destination)) {
                results.add(trip);
            }
        }

        return results;
    }
}

/* =========================
   SERVICE API
   ========================= */

class RouteService {
    private final OkHttpClient client;
    private final Gson gson;
    private final String apiKey;

    public RouteService(String apiKey) {
        this.client = new OkHttpClient();
        this.gson = new Gson();
        this.apiKey = apiKey;
    }

    public RouteInfo calculateRoute(Address start, Address end) throws IOException {

        System.out.println("test");
        String url = String.format(Locale.US,
                "https://graphhopper.com/api/1/route?" +
                        "point=%f,%f&point=%f,%f&profile=car&locale=fr&instructions=true&" +
                        "calc_points=true&points_encoded=false&key=%s",
                start.getLatitude(), start.getLongitude(),
                end.getLatitude(), end.getLongitude(),
                apiKey
        );

        Request request = new Request.Builder()
                .url(url)
                .build();

        try (Response response = client.newCall(request).execute()) {
            String body = response.body() != null ? response.body().string() : "";

            System.out.println("Code HTTP : " + response.code());
            System.out.println("Réponse brute : " + body);

            if (!response.isSuccessful()) {
                throw new IOException("Erreur HTTP " + response.code() + " : " + body);
            }

            RouteResponse routeResponse = gson.fromJson(body, RouteResponse.class);

            if (routeResponse == null || routeResponse.paths == null || routeResponse.paths.length == 0) {
                throw new IOException("Aucun itinéraire trouvé. Réponse : " + body);
            }

            double distance = routeResponse.paths[0].distance;
            long time = routeResponse.paths[0].time;

            return new RouteInfo(distance, time);
        }
    }
}

class RouteInfo {
    final double distanceMeters;
    final long durationMs;

    public RouteInfo(double distanceMeters, long durationMs) {
        this.distanceMeters = distanceMeters;
        this.durationMs = durationMs;
    }
}

/* =========================
   CLASSES POUR LE JSON
   ========================= */

class RouteResponse {
    Path[] paths;
}

class Path {
    double distance;
    long time;
}