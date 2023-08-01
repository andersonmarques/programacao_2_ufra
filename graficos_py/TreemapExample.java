import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.TilePane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

import java.util.Arrays;
import java.util.List;

public class TreemapExample extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        // Dados
        List<String> labels = Arrays.asList("Matriculados", "Aprovados", "Reprovados");
        List<Double> quantidades = Arrays.asList(13.0, 12.0, 1.0);

        // Cores das categorias
        List<Color> cores = Arrays.asList(Color.web("#ff9999"), Color.web("#66b3ff"), Color.web("#99ff99"));

        // Criação dos retângulos e rótulos
        TilePane tilePane = new TilePane();
        for (int i = 0; i < labels.size(); i++) {
            double tamanho = quantidades.get(i);
            Rectangle rectangle = new Rectangle(tamanho * 50, tamanho * 50, cores.get(i));
            Label label = new Label(labels.get(i) + " (" + tamanho + ")");
            tilePane.getChildren().addAll(rectangle, label);
        }

        // Configuração do layout
        BorderPane root = new BorderPane();
        root.setCenter(tilePane);

        // Configuração da cena e palco
        Scene scene = new Scene(root, 400, 400);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Treemap Squarified Example");
        primaryStage.show();
    }
}
