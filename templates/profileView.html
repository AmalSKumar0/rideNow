<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="shortcut icon" href="images/favicon.ico" title="Favicon" />
  <title>Document</title>
  
</head>
<?php
//connecting to database
$conn = mysqli_connect("localhost", "root", "", "rikshawhub");
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
session_start();
//both are same cause the user is viewing his won profile
//fetching data of the driver for the view
$stmt = $conn->prepare("SELECT * FROM driver WHERE driver_id = ?");
$stmt->bind_param("i", $_SESSION['did']);
$stmt->execute();
$result = $stmt->get_result();
$user = $result->fetch_assoc();
$name = $user['name'];
$email = $user['email'];
$gender = $user['gender'];
$address = $user['address'];
$phone = $user['phone_no'];
$licence = $user['licence_no'];
$vehicle = $user['vehicle_no'];
$img = $user['Auto_img'];
$date = $user['created_at'];
$rating = $user['rating'];
if (isset($_GET['back'])) {
  // session_destroy();
  echo '<script>window.location.href="passenger.php";</script>';
}
?>

<body>
  <div class="area">
    <ul class="circles">
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
    </ul>
  </div>
  <link rel="stylesheet" href="styles/profile.css">
  <!-- the view for profile -->
  <div class="card into">
    <div class="img-avatar">
      <img src="uploads/<?php echo $img; ?>" alt="profilePic">
    </div>
    <div class="card-text">
      <div class="portada">
        <img src="images/profile-bg.jpg" style="width: 100%; height: 100%; border-top-left-radius: 20px; border-bottom-left-radius: 20px; object-fit: cover;">
      </div>
      <div class="title-total">
        <div class="title"><?php echo 'Driver'; ?></div>
        <h2><?php echo strtoupper($name); ?></h2></BR>
        <!-- soting deails for driver and passenger -->
        <div class="details">
          <li>Gender:<?php echo $gender; ?></li>
          <li>Email:<?php echo $email; ?></li>
          <li>Phone no:<?php echo $phone; ?></li>
          <li>Address:<?php echo $address; ?></li>
          <li>Rating:<?php echo $rating; ?>☆ </li>
          <li>Licence no:<?php echo $licence; ?></li>
          <li>Vehicle no:<?php echo $vehicle; ?></li>
          <li>Joined on:<?php echo $date; ?></li>
        </div>
        <div class="actions">
          <!-- button for user interaction -->
          <!-- Button to open the modal -->
          <button id="openModalBtn" class="view-reviews-btn">REVIEWS</button>

          <!-- Modal Structure -->
          <div id="reviewModal" class="modal">
                <div class="modal-content">
                  <span class="close">&times;</span>
                  <h2 class="review-title">Driver Reviews</h2>
                  <?php include 'snippets/reviewViewer.php'; ?>
                </div>
              </div>

          <form method="get" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>">
            <button name="back" value="true">BACK</button>
          </form>
        </div>
      </div>
    </div>
  </div>
  <script src="scripts/profileWindow.js"></script>
</body>

</html>