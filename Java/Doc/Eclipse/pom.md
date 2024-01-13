# 1.標準設定
## 1-1.Java Version指定

```
	<build>
		<plugins>
			<!-- コンパイル設定 -->
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-compiler-plugin</artifactId>
				<version>3.10.1</version>
				<configuration>
					<release>11</release>
				</configuration>
			</plugin>
		</plugins>
	</build>
```

# 2.追加ライブラリ

## 2-1.logger

```
		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-classic</artifactId>
			<version>1.2.11</version>
		</dependency>

		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-core</artifactId>
			<version>1.2.11</version>
		</dependency>
```

## 2-2.JUnit

```
		<dependency>
			<groupId>org.junit.jupiter</groupId>
			<artifactId>junit-jupiter</artifactId>
			<version>5.8.2</version>
			<scope>test</scope>
		</dependency>
```

buildのpluginを追加。mavenからテストを行うのに必要。

```
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-surefire-plugin</artifactId>
				<version>3.0.0-M5</version>

				<configuration>
				<!-- テストが失敗してもレポートを作成する -->
					<testFailureIgnore>true</testFailureIgnore>
				</configuration>
			</plugin>

			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-surefire-report-plugin</artifactId>
				<version>3.0.0-M5</version>
				<executions>
					<execution>
						<phase>test</phase>
						<goals>
							<goal>report</goal>
						</goals>
					</execution>
				</executions>
			</plugin>
```

```
		<dependency>
			<groupId>org.assertj</groupId>
			<artifactId>assertj-core</artifactId>
			<version>3.23.1</version>
			<scope>test</scope>
		</dependency>
```