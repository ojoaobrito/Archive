/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bases1;

import bases1.Registo;
import bases1.ListaRegistos;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

/**
 *
 * @author Utilizador
 */
public class SqlManager {
    
    
    private String connectionUrl;

    private String host, username, database, password;
    private int port;
    
    Connection con;

    public SqlManager() {
        
        host = "localhost";
        port = 1433;
        username = "Joao";
        password = "Bases2018";
        database = "Registos";
        
        openConnection();
    }
    
    private void openConnection() {
        
        connectionUrl = "jdbc:sqlserver://" + host + ":" + port + ";user=" + username + ";password=" + password + ";databaseName=" + database + ";integratedSecurity=true;";
        
        try {
            
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            this.con = DriverManager.getConnection(connectionUrl);
            
        }catch(Exception e){
            e.printStackTrace();
        }
            
        createTables();
    }
    
    public void closeConnection() {
        closeConnection(this.con);
    }
    
    public void closeConnection(Connection con) {
        try {
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public Connection getConnection() {
        return this.con;
    }
    
     public void createTables() {
        Connection c = null;
        try {
            c = getConnection();
            Statement statement = c.createStatement();
            
            /**
            String clientTable = "CREATE TABLE IF NOT EXISTS "
                    + "clients(numero SMALLINT PRIMARY KEY, telefone SMALLINT, nome varchar(50), mail varchar(40), morada varchar(70), data varchar(30));";
            String productTable = "CREATE TABLE IF NOT EXISTS "
                    + "products(codigo SMALLINT PRIMARY KEY, quantidade SMALLINT, designacao varchar(40))";
            **/
            
            String registoTable = "CREATE TABLE IF NOT EXISTS" + " Registo(Num INT, Nome varchar(50)";
            
            statement.execute(registoTable);
            
            statement.close();
        } catch (SQLException e) {
            //e.printStackTrace();
        } finally {
            //closeConnection(c);
        }
    }
     
    public Registo getRegisto(int numero) {
        Connection c = null;
        try {
            c = getConnection();
            PreparedStatement preparedStatement = c.prepareStatement("SELECT * FROM Registo WHERE Num= " +numero);
            preparedStatement.setInt(1, numero);
            ResultSet resultSet = preparedStatement.executeQuery();
            Registo registo = null;
            if (resultSet.next()) {
                registo = new Registo(resultSet.getString("Nome"), numero);      
            }
            resultSet.close();
            preparedStatement.close();
            return registo;
            
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            //closeConnection(c);
        }
        return null;
    }
    
    public ArrayList<Registo> getRegistos() {
        Connection c = null;
        
        try {
            c = getConnection();
            PreparedStatement preparedStatement = c.prepareStatement("SELECT * FROM Registo");
            ResultSet resultSet = preparedStatement.executeQuery();
            ArrayList<Registo> registos = new ArrayList();
            while(resultSet.next()) {
                Registo registoTemp = new Registo(resultSet.getString("Nome"), resultSet.getInt("Num"));
                registos.add(registoTemp);
            }
            resultSet.close();
            preparedStatement.close();
            return registos;
            
        } catch (SQLException e) {
            e.printStackTrace();
            
        } finally {
            //closeConnection(c);
        }
        return null;
    }
    
    public void saveRegisto(Registo registo) {
        Connection c = null;
        try {
            c = getConnection();
            PreparedStatement statement = c.prepareStatement("SELECT Num FROM Registo WHERE Num=?");
            statement.setInt(1, registo.getNumero());
            ResultSet resultSet = statement.executeQuery();
            
            if (resultSet.next()) {
                PreparedStatement preparedStatement = c.prepareStatement("UPDATE Registo SET Nome=? WHERE Num=?");
                preparedStatement.setInt(1, registo.getNumero());
                preparedStatement.setString(2, registo.getNome());
                preparedStatement.executeUpdate();
                preparedStatement.close();
            } 
            
            else {
                PreparedStatement preparedStatement = c.prepareStatement("INSERT INTO Registo(Num, Nome) VALUES(?,?);");
                preparedStatement.setInt(1, registo.getNumero());
                preparedStatement.setString(2, registo.getNome());
                preparedStatement.executeUpdate();
                preparedStatement.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            //closeConnection(c);
        }
    }
}
