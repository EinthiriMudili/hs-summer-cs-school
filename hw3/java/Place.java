public class Place {

    public double latitude;
    public double longitude;

    public double dLat;
    public double dLon;

    public Place(double latitude, double longitude) {
        this.latitude = latitude;
        this.longitude = longitude;
    }



    public String distance(Place other) {

        // TODO
        dLat = (other.latitude - this.latitude) * Math.PI / 180.0;
        System.out.println("distance_latitude: " + Double.toString(dLat));
        dLon = (other.longitude - this.longitude) * Math.PI / 180.0;
        System.out.println("distance_longitude: " + Double.toString(dLon));
        this.latitude = this.latitude * Math.PI / 180.0;
        other.longitude = other.longitude * Math.PI/180.0;
        Double a = (Math.pow(Math.sin(dLat / 2), 2)) +
                ((Math.pow(Math.sin(dLon / 2), 2)) *
                        (Math.cos(this.latitude) * Math.cos(other.latitude)));
        double rad = 3961;
        Double c = 2 * Math.asin(Math.sqrt(a));
        String distance = Double.toString(rad*c);
        System.out.println("distance between self and other place in miles: " + Double.toString(rad*c));
        return distance;
    }

    @Override
    public String toString() {
        return this.latitude + ", " + this.longitude;
    }
}